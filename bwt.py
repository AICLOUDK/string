# python3
class BWT:
    def __init__(self, text):
        self.bwt = self.transform(text)

    def transform(self, text):
        rotations = [text[i:] + text[:i] for i in range(len(text))]
        rotations.sort()
        return "".join(r[-1] for r in rotations)

if __name__ == "__main__":
    text = input().strip()
    print(BWT(text).bwt)