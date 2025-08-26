#include <cstdio>
#include <map>

#define N 150005
#define INF 2147483647
#define LOGN 19
using namespace std;

int n, q, u[N], v[N], s[N], t[N];  // input
map<pair<int, int>, int> edgemap;  // u-v => TREENODE
int up[N][LOGN];                   // up[i][j]: treenode_i's (2^j)-th ancestor

struct TREENODE {
    int parent, depth;
    int nodes[3];
};
TREENODE tree[N];
// tree[i].nodes = {i, u, v}, i: new graph node, u-v: based edge, i >= 3

struct DISMAT {
    int data[3][3];
};
DISMAT dis[N][LOGN];
/*
dis[i][j].data: distance matrix
- row: nodes of tree[i]
- col: nodes of tree[up[i][j]]

dis[i][j].data[p][q]: minimum distance from tree[i].nodes[p] to tree[up[i][j]].nodes[q]
*/

DISMAT operator*(const DISMAT& a, const DISMAT& b) {
    DISMAT res;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            res.data[i][j] = INF;
            for (int k = 0; k < 3; k++) {
                res.data[i][j] = min(res.data[i][j], a.data[i][k] + b.data[k][j]);
            }
        }
    }
    return res;
}

void buildTree() {
    tree[3] = TREENODE({0, 0, {3, 1, 2}});
    edgemap[{1, 2}] = edgemap[{2, 3}] = edgemap[{1, 3}] = 3;
    for (int i = 4; i <= n; i++) {
        if (u[i] > v[i]) swap(u[i], v[i]);
        int parent = edgemap[{u[i], v[i]}];
        tree[i] = {parent, tree[parent].depth + 1, {i, u[i], v[i]}};
        edgemap[{u[i], i}] = i;
        edgemap[{v[i], i}] = i;
    }
}

/*
disInit(k): initialize dis[k][0] for tree[k]

e.g.

   u --- v
  / \   /
 /   \ /
k --- p

p = tree[k].parent
tree[p].nodes = {p, u, v}  (based edge: u-v)
tree[k].nodes = {k, p, u}  (based edge: p-u)

dis[k][0].data:
   p  u  v
k  1  1  2
p  0  1  1
u  1  0  1
*/
void disInit(int k) {
    int p = tree[k].parent;
    if (p == 0) return;
    int u = tree[k].nodes[1], v = tree[k].nodes[2];
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (i == 0) {
                if (tree[p].nodes[j] == u || tree[p].nodes[j] == v)
                    dis[k][0].data[i][j] = 1;
                else
                    dis[k][0].data[i][j] = 2;
            } else {
                if (tree[p].nodes[j] == tree[k].nodes[i])
                    dis[k][0].data[i][j] = 0;
                else
                    dis[k][0].data[i][j] = 1;
            }
        }
    }
}

void buildBinaryLifting() {
    // up
    for (int i = 3; i <= n; i++) {
        up[i][0] = tree[i].parent;
        for (int j = 1; (1 << j) < n; j++) {
            int mid = up[i][j - 1];
            up[i][j] = mid ? up[mid][j - 1] : 0;
        }
    }
    // dis
    for (int i = 3; i <= n; i++) {
        disInit(i);
        for (int j = 1; (1 << j) < n; j++) {
            int mid = up[i][j - 1];
            // dis[i][j-1]:   distance matrix of tree[i] -> tree[mid]
            // dis[mid][j-1]: distance matrix of tree[mid] -> tree[up[i][j]]
            if (mid) dis[i][j] = dis[i][j - 1] * dis[mid][j - 1];
        }
    }
}

int getLCA(int u, int v) {
    if (tree[u].depth < tree[v].depth) swap(u, v);
    for (int i = LOGN - 1; i >= 0; i--) {
        if (up[u][i] && tree[up[u][i]].depth >= tree[v].depth) {
            u = up[u][i];
        }
    }
    if (u == v) return u;
    for (int i = LOGN - 1; i >= 0; i--) {
        if (up[u][i] != up[v][i]) {
            u = up[u][i];
            v = up[v][i];
        }
    }
    return tree[u].parent;
}

DISMAT getDistanceMatrix(int u, int ancestor) {
    DISMAT res = {{{0, 1, 1}, {1, 0, 1}, {1, 1, 0}}};
    for (int i = LOGN - 1; i >= 0; i--) {
        if (up[u][i] && tree[up[u][i]].depth >= tree[ancestor].depth) {
            res = res * dis[u][i];
            u = up[u][i];
        }
    }
    return res;
}

int query(int s, int t) {
    // s,t: graph nodes
    // u,v: tree nodes
    int u = s < 3 ? 3 : s;
    int v = t < 3 ? 3 : t;
    int lca = getLCA(u, v);

    DISMAT mu = getDistanceMatrix(u, lca);
    DISMAT mv = getDistanceMatrix(v, lca);

    int ans = INF;
    int iu = s < 3 ? s : 0;
    int iv = t < 3 ? t : 0;
    for (int j = 0; j < 3; j++) {
        ans = min(ans, mu.data[iu][j] + mv.data[iv][j]);
    }

    return ans;
}

int main() {
    scanf("%d", &n);
    for (int i = 4; i <= n; i++) {
        scanf("%d %d", &u[i], &v[i]);
    }
    scanf("%d", &q);
    for (int i = 0; i < q; i++) {
        scanf("%d %d", &s[i], &t[i]);
    }
    buildTree();
    buildBinaryLifting();
    for (int i = 0; i < q; i++) {
        printf("%d\n", query(s[i], t[i]));
    }
    return 0;
}
/*
12
1 2
2 4
1 3
4 2
1 2
4 2
4 9
10 4
3 6
5
4 4
1 8
1 7
11 3
12 11
*/
// answer: 0 1 2 3 4
// g++ -std=c++17 -o exp exp.cpp; ./exp
