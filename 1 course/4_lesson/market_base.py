def market_base(table):
    base = {}
    for note in table:
        note = note.strip().split()
        if len(note) == 0:
            return
        base.setdefault(note[0],{})
        base[note[0]][note[1]] = base[note[0]].get(note[1],0) + int(note[2])
    for person_note in sorted(base):
        print(f"{person_note}:")
        base[person_note] = sorted(base[person_note].items(), key=lambda x: x[0])
        for product, count in base[person_note]:
            print(product, count)
infile = open("input.txt")
market_base(infile.readlines())