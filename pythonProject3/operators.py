print(not(4==5)and(8+5==13)or(5<=9)and(90>=100)or(9<6))
      #(  not f and t or f and f or f
      #     f or f or f => f or f=>not (f)=>true
print(3 in (3,5 and 3) and not(True))or (4==5)
      #  t in t  and f or f=> t and f=>f
print(3 not in (3,5 and 3)and not(True))or(4==5)
      # t not in t and f or f=> f and   f=>f