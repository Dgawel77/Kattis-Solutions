fact = [
    1,
    1,
    2,
    6,
    24,
    120,
    720,
    5040,
    40320,
    362880,
    3628800,
    39916800,
    479001600,
    6227020800,
    87178291200,
    1307674368000,
    20922789888000,
    355687428096000,
    6402373705728000,
    121645100408832000,
    2432902008176640000,
    51090942171709440000,
    1124000727777607680000,
    25852016738884976640000,
    620448401733239439360000,
    15511210043330985984000000,
    403291461126605635584000000,
    10888869450418352160768000000,
    304888344611713860501504000000,
    8841761993739701954543616000000,
    265252859812191058636308480000000,
    8222838654177922817725562880000000,
    263130836933693530167218012160000000,
    8683317618811886495518194401280000000,
    295232799039604140847618609643520000000,
    10333147966386144929666651337523200000000,
    371993326789901217467999448150835200000000,
    13763753091226345046315979581580902400000000,
    523022617466601111760007224100074291200000000,
    20397882081197443358640281739902897356800000000,
    815915283247897734345611269596115894272000000000,
    33452526613163807108170062053440751665152000000000,
    1405006117752879898543142606244511569936384000000000,
    60415263063373835637355132068513997507264512000000000,
    2658271574788448768043625811014615890319638528000000000,
    119622220865480194561963161495657715064383733760000000000,
    5502622159812088949850305428800254892961651752960000000000,
    258623241511168180642964355153611979969197632389120000000000,
    12413915592536072670862289047373375038521486354677760000000000,
    608281864034267560872252163321295376887552831379210240000000000]


def getsum(BITTree, i):
    s = 0
    i = i+1
    while i > 0:
        s += BITTree[i]
        i -= i & (-i)
    return s


def updatebit(BITTree, n, i, v):
    i += 1
    while i <= n:
        BITTree[i] += v
        i += i & (-i)


def construct(arr, n):
    BITTree = [0]*(n+1)

    for i in range(n):
        updatebit(BITTree, n, i, arr[i])
    return BITTree


class TrieNode:
    def __init__(self):
        self.children = [None]*27
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, ch):
        return ord(ch)-ord('a')

    def insert(self, key, place):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
        pCrawl.isEndOfWord = True
        pCrawl.children[26] = place

    def search(self, key):
        startNode = self.root
        pCrawl = self.root
        length = len(key)
        numberList = []
        for level in range(length):
            index = self._charToIndex(key[level])
            if pCrawl.children[index].isEndOfWord:
                numberList.append(pCrawl.children[index].children[26])
                pCrawl = startNode
            else:
                pCrawl = pCrawl.children[index]
        return numberList


n, k = map(int, input().split())
t = Trie()
keys = []
for _ in range(n):
    keys.append(input())
keys.sort()
for pos, key in enumerate(keys):
    t.insert(key, pos+1)
numberOrder = t.search(input())
print(numberOrder)
ans = 0
BITTree = construct([1 for _ in range(n)], n)
for p, number in enumerate(numberOrder):
    pos = p+1
    ans = (ans + getsum(BITTree, number-2) * (fact[n-pos] // fact[n-k]))
    print(getsum(BITTree, number-2), n-pos, n-k, number-2)
    updatebit(BITTree, n, number, -1)

print(ans)
# print("Sum of elements in arr[0..5] is " + str(getsum(BITTree, 4)))

# #freq[3] += 6
# updatebit(BITTree, n, 3, -1)
# print("Sum of elements in arr[0..5]" +
#       " after update is " + str(getsum(BITTree, 4)))
