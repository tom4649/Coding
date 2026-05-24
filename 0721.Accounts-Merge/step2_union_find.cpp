#include <vector>
#include <string>
#include <unordered_map>
#include <set>
#include <numeric>
#include <algorithm>

class UnionFind {
public:
    std::vector<int> parent;
    std::vector<int> size;

    UnionFind(int n) {
        parent.resize(n);
        std::iota(parent.begin(), parent.end(), 0);
        size.assign(n, 1);
    }

    int find(int x) {
        if (x != parent[x]) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void union_op(int x, int y) {
        int parent_x = find(x);
        int parent_y = find(y);

        if (parent_x == parent_y) {
            return;
        }

        if (size[parent_x] < size[parent_y]) {
            std::swap(parent_x, parent_y);
        }

        parent[parent_y] = parent_x;
        size[parent_x] += size[parent_y];
        return;
    }
};

class Solution {
public:
    std::vector<std::vector<std::string>> accountsMerge(std::vector<std::vector<std::string>>& accounts) {
        UnionFind union_find(accounts.size());
        std::unordered_map<std::string, int> mail_to_account_index;
        std::vector<std::vector<std::string>> accounts_merged;

        for (int account_index = 0; account_index < accounts.size(); ++account_index) {
            for (size_t i = 1; i < accounts[account_index].size(); ++i) {
                const std::string& email = accounts[account_index][i];
                if (mail_to_account_index.count(email)) {
                    union_find.union_op(account_index, mail_to_account_index[email]);
                } else {
                    mail_to_account_index[email] = account_index;
                }
            }
        }

        std::unordered_map<int, std::vector<std::string>> root_to_emails;
        for (int account_index = 0; account_index < accounts.size(); ++account_index) {
            int root = union_find.find(account_index);
            for (size_t i = 1; i < accounts[account_index].size(); ++i) {
                root_to_emails[root].push_back(accounts[account_index][i]);
            }
        }

        for (auto& [root, emails] : root_to_emails) {
            std::set<std::string> unique_emails(emails.begin(), emails.end());

            std::vector<std::string> merged_row;
            merged_row.push_back(accounts[root][0]);
            for (const auto& email : unique_emails) {
                merged_row.push_back(email);
            }
            accounts_merged.push_back(merged_row);
        }

        return accounts_merged;
    }
};
