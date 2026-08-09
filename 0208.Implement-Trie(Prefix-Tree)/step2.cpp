#include <array>
#include <memory>
#include <string>

class Trie {
    class TrieNode {
    public:
        std::array<std::unique_ptr<TrieNode>, 26> children{};
        bool is_end = false;
    };

    std::unique_ptr<TrieNode> root_;

    const TrieNode* searchChild(const std::string& word) const {
        const TrieNode* node = root_.get();
        for (char c : word) {
            const int i = c - 'a';
            if (!node->children[i]) {
                return nullptr;
            }
            node = node->children[i].get();
        }
        return node;
    }

public:
    Trie() : root_(std::make_unique<TrieNode>()) {}

    void insert(std::string word) {
        TrieNode* node = root_.get();
        for (char c : word) {
            const int i = c - 'a';
            if (!node->children[i]) {
                node->children[i] = std::make_unique<TrieNode>();
            }
            node = node->children[i].get();
        }
        node->is_end = true;
    }

    bool search(std::string word) {
        const TrieNode* node = searchChild(word);
        return node != nullptr && node->is_end;
    }

    bool startsWith(std::string prefix) {
        return searchChild(prefix) != nullptr;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */