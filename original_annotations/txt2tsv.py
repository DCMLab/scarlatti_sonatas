import re, os
from fractions import Fraction as frac
import pandas as pd

dcml_regex = re.compile(r"""
                                ^(?P<first>
                                  (\.?
                                    ((?P<globalkey>[a-gA-G](b*|\#*))\.)?
                                    ((?P<localkey>((b*|\#*)(VII|VI|V|IV|III|II|I|vii|vi|v|iv|iii|ii|i)/?)+)\.)?
                                    ((?P<pedal>((b*|\#*)(VII|VI|V|IV|III|II|I|vii|vi|v|iv|iii|ii|i)/?)+)\[)?
                                    (?P<chord>
                                        (?P<numeral>(b*|\#*)(VII|VI|V|IV|III|II|I|vii|vi|v|iv|iii|ii|i|Ger|It|Fr|@none))
                                        (?P<form>(%|o|\+|M|\+M))?
                                        (?P<figbass>(7|65|43|42|2|64|6))?
                                        (\((?P<changes>((\+|-|\^|v)?(b*|\#*)\d)+)\))?
                                        (/(?P<relativeroot>((b*|\#*)(VII|VI|V|IV|III|II|I|vii|vi|v|iv|iii|ii|i)/?)*))?
                                    )
                                    (?P<pedalend>\])?
                                  )?
                                  (\|(?P<cadence>((HC|PAC|IAC|DC|EC|PC)(\..+?)?)))?
                                  (?P<phraseend>(\\\\|\}\{|\{|\})
                                  )?
                                 )
                                 (-
                                  (?P<second>
                                    ((?P<globalkey2>[a-gA-G](b*|\#*))\.)?
                                    ((?P<localkey2>((b*|\#*)(VII|VI|V|IV|III|II|I|vii|vi|v|iv|iii|ii|i)/?)+)\.)?
                                    ((?P<pedal2>((b*|\#*)(VII|VI|V|IV|III|II|I|vii|vi|v|iv|iii|ii|i)/?)+)\[)?
                                    (?P<chord2>
                                        (?P<numeral2>(b*|\#*)(VII|VI|V|IV|III|II|I|vii|vi|v|iv|iii|ii|i|Ger|It|Fr|@none))
                                        (?P<form2>(%|o|\+|M|\+M))?
                                        (?P<figbass2>(7|65|43|42|2|64|6))?
                                        (\((?P<changes2>((\+|-|\^|v)?(b*|\#*)\d)+)\))?
                                        (/(?P<relativeroot2>((b*|\#*)(VII|VI|V|IV|III|II|I|vii|vi|v|iv|iii|ii|i)/?)*))?
                                    )
                                    (?P<pedalend2>\])?
                                  )?
                                  (\|(?P<cadence2>((HC|PAC|IAC|DC|EC|PC)(\..+?)?)))?
                                  (?P<phraseend2>(\\\\|\}\{|\{|\})
                                  )?
                                 )?
                                $
                                """,
                        re.VERBOSE)

def load_txt(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines


def treat_beat(beat, subbeat, beat_unit=frac(1, 4)):
    beat_unit = frac(beat_unit)
    subbeat_division = frac(1, 2) if beat_unit.numerator % 3 else frac(1,3)
    offset = (int(beat) - 1) * beat_unit
    if subbeat is not None:
        offset += (int(subbeat) - 1 ) * subbeat_division * beat_unit
    return frac(offset)


def line2labels(line, beat_unit=frac(1,4)):
    if line[0] == '@':
        #print(line.strip('\n'))
        return None, None
    elements = line.split()
    if len(elements) == 0:
        return None, None
    try:
        mn = int(elements[0][1:])
    except ValueError:
        mn = elements[0][1:]
        if not re.match(r"\d+[a-z]", mn):
            print(line)
            raise

    def label_result():
        nonlocal beat, label
        if beat is not None and label != '':
            if not re.match(dcml_regex, label):
                print(f"Label doesn't match: {label}")
            beat2label[beat] = label
            beat, label = None, ''

    beat_re = r"^(?P<beat>\d{1,2})(?:\.(?P<subbeat>\d)?)?$"
    beat2label = {}
    beat, label = None, ''
    for e in elements[1:]:
        m = re.match(beat_re, e)
        if m is None:
            if e[0] == '.':
                append = e[1:]
            elif e.lower() in ('@alt', '@alt:'):
                append = '-'
            elif e == '@none':
                append = e
            elif e[0] == '@':
                append = '|' + e[1:]
            else:
                append = e
            label += append
        else:
            label_result()
            beat, subbeat = m['beat'], m['subbeat']
            beat = treat_beat(beat, subbeat, beat_unit)
    label_result()
    return mn, beat2label

meter2beat_unit = {
    '2/4': frac(1,4),
    '3/4': frac(1,4),
    '4/4': frac(1,4),
    '3/8': frac(1,8),
    '6/8': frac(1,8),
    '2/2': frac(1,2),
    '12/8': frac(1,8),
}

def lines2df(lines):
    vals = []
    for l in lines:
        if l[:6] == '@meter':
            meter = l[7:].strip()
            beat_unit = meter2beat_unit[meter]
            break
    for l in lines:
        mn, beat2label = line2labels(l, beat_unit)
        if mn is not None:
            vals.extend([(mn, beat, label) for beat, label in beat2label.items()])
    return pd.DataFrame(vals, columns=['mn', 'mn_offset', 'label'])

def txt2df(path):
    lines = load_txt(path)
    return lines2df(lines)

if __name__ == "__main__":

    SOURCE = '.'
    TARGET = '../harmonies'

    for fname in sorted(os.listdir(SOURCE)):
        fn, ext = os.path.splitext(fname)
        if ext != '.txt':
            continue
        print(fname)
        df = txt2df(os.path.join(SOURCE, fname))
        if fn in ('K018', 'K019', 'K022', 'K049'):
            df.columns = ['mc', 'mc_onset', 'label']
        if fn == 'K027':
            df.mn -= 1
        tsv_path = os.path.join(TARGET, fn + '.tsv')
        df.to_csv(tsv_path, sep='\t', index=False)
        print("Written " + tsv_path)
