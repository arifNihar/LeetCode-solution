class Solution {
public:
vector<int> beautifulArray(int N){
    vector<int>ans;
    if(N==1){
        ans.push_back(1);return ans;
    }
    else {
        vector<int>ve = beautifulArray((N+1)/2);
        int sz = ve.size();
        for(int it=0;it<sz;it++)ans.push_back(2*ve[it]-1);
        vector<int>vv = beautifulArray(N/2);
        sz = vv.size();
        for(int it=0;it<sz;it++)ans.push_back(2*vv[it]);
    }
    return ans;
}
};