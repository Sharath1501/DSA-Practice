#include<bits/stdc++.h>
using namespace std;

// vector<int> traversal(int v,vector<int>adj[]){
//     vector<int> vis(v , 0);
//     vis[0] =1;
//     queue<int> q;
//     q.push(0);
//     vector<int> bfs;
//     while(!q.empty()){
//         int node = q.front();
//         q.pop();
//         bfs.push_back(node);
//         for(auto it:adj[node]){
//             if(!vis[it]){
//                 vis[it] =1;
//                 q.push(it);
//             }
//         }
//     }
//     return bfs;
// }
// int main(){

//     int n,m;
//     cin>>n>>m;
//     vector<int> adj[n];
//     for(int i=0;i<m;i++){
//         int u,v;
//         cin>>u>>v;
//         adj[u].push_back(v);
//         adj[v].push_back(u);
//     }
//     vector<int> res = traversal(n,adj);
//     for(int node:res){
//         cout<<node<<" ";
//     }
//     return 0;
// }

vector<int> traversal(int v,vector<int>adj[]){
    vector<int> vis(v,0);
    vis[0] =1;
    vector<int> bfs;
    queue<int> q;
    q.push(0);
    while(!q.empty()){
        int node = q.front();
        q.pop();
        bfs.push_back(node);
        for(int it:adj[node]){
            if(!vis[it]){
                vis[it]=1;
                q.push(it);
            }
        }
    }
    return bfs;
}
void dfs(int start,vector<int> adj[],vector<int> &vis,vector<int> &ls){
    vis[start] =1;
    ls.push_back(start);

    for(auto it:adj[start]){
        if(!vis[it]){
            dfs(it,adj,vis,ls);
        }
    }
}
vector<int> dfstraversal(int v,vector<int> adj[]){
    vector<int> vis(v,0);
    int start =0;
    vector<int> ls;
    dfs(start,adj,vis,ls);
    return ls;

}

int main(){
    int n,m;
    cin>>n>>m;
    vector<int> adj[n];
    for(int i=0;i<m;i++){
        int u,v;
        cin>>u>>v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> re = traversal(n,adj);
    for(auto it : re){
        cout<<it<<" ";
    }
    vector<int> res = dfstraversal(n,adj);
    for(auto it : res){
        cout<<it<<" ";
    }
}

