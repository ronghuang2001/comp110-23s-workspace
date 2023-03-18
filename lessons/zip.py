"""zip."""
def zip(a: list[str], b: list[int]) -> dict[str,int]:
    if len(a)!= len(b) or len(a) == 0 or len(b) ==0:
       return dict()
    else:
        dictionary: dict[str,int] = dict()
        idx: int = 0
        for idx in range(0,len(a),1):
            dictionary[a[idx]] = b[idx]
            idx = idx + 1
        return dictionary