vector<int> traversal(int v,vector<int>adj[]){
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