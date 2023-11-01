class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:  return False
        hand.sort()
        l, r = 0, 0
        visited = set()
        prevElement = -1
        while len(visited) != len(hand) and r < len(hand) and l < len(hand):
            if r not in visited:
                if prevElement == -1:
                    prevElement = hand[r]
                    curSize = 1
                    visited.add(r)
                elif hand[r] == prevElement + 1:
                    prevElement = hand[r]
                    visited.add(r)
                    curSize += 1
                if curSize == groupSize:
                    l += 1
                    prevElement = -1
                    r = l
                    continue
            r += 1

        return True if len(visited) == len(hand) else False
