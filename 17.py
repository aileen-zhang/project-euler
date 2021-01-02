# letter counts in numbers < 1000

total = 0

total += 900 * len("hundred")
total += 10 * len("teneleventwelvethirteenfourteen" +
                  "fifteensixteenseventeeneighteennineteen")
total += 100 * len("twentythirtyfortyfiftysixtyseventyeightyninety")
total += 190 * len("onetwothreefourfivesixseveneightnine")
total += 891 * len("and")
total += len("onethousand")

print(total)
