sex = """27 75 00 01 31 00 0a 00  00 00 00 00 00 09 eb 00
00 00 24 63 36 33 30 66  39 32 64 37 35 39 37 31
38 35 33 33 66 35 32 35  36 34 33 64 62 32 63 37
63 34 62 37 65 65 61 00  00 00 13 00 00 00 00 00
00 00 6f 00 00 00 40 63  66 38 62 33 64 32 62 61
38 30 66 33 32 62 38 31  32 35 66 39 62 37 62 65
39 37 66 35 35 33 36 33  33 66 35 66 31 30 33 66
63 37 35 32 37 63 33 33  63 35 61 63 39 65 30 39
64 31 35 33 66 32 30 00  00 00 00 00 00 00 10 63  
61 63 63 37 34 31 63 38  31 30 35 31 34 65 62 ff
ff ff ff 00 00 00 07 4a  41 54 2d 4c 58 31 01 11
00 00 00 05 72 75 2d 52  55 00 00 00 24 39 33 33
37 66 35 36 64 2d 39 33  39 35 2d 34 37 30 66 2d
61 31 38 38 2d 32 62 34  31 32 39 64 36 65 66 62
62 00 00 00 01 39 01 00  00 00 00 00 00 00 10 63
61 63 63 37 34 31 63 38  31 30 35 31 34 65 62 00
00 00 00 01 00 00 00 00  00 00 05 b0 02 00 00 00
00 00 00 00 00 00 00 00  06 31 39 2e 31 31 31 00
00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00
00 00 00 00 ff ff ff ff"""
dudka = sex.replace(" ", "")
eblan = dudka.replace("""
""", "")
print(eblan)