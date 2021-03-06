#include <iostream>

using namespace std;

class Node
{
	public:
		static const int MAX_CHILD = 10;
		bool is_end;
		Node *child[MAX_CHILD];
	public:
		Node(): is_end(false)
		{
			for (int i = 0; i < MAX_CHILD; ++i)
			{
				child[i] = NULL;
			}
		}
};

class Trie
{
	private:
		Node *root;
		void remove_trie(Node *);
	public:
		Trie();
		~Trie();
		void insert(const string &s);
		bool search(const string &s);
};

Trie::Trie()
{
	root = new Node();
}

Trie::~Trie()
{
	remove_trie(root);
}

void Trie::remove_trie(Node *root)
{
	if (root == NULL)
	{
		return;
	}
	for (int i = 0; i < Node::MAX_CHILD; ++i)
	{
		remove_trie(root->child[i]);
	}
	delete root;
}

void Trie::insert(const string &s)
{
	Node *cur = root;
	for (size_t i = 0; i < s.length(); ++i)
	{
		int d = s[i] - '0';
		if (cur->child[d] == NULL)
		{
			cur->child[d] = new Node();
		}
		cur = cur->child[d];
	}
	cur->is_end = true;
}

bool Trie::search(const string &s)
{
	Node *cur = root;
	for (size_t i= 0; i < s.length(); ++i)
	{
		int d = s[i] - '0';
		if (cur->is_end == true)
		{
			return true;
		}
		else if (cur->child[d] == NULL)
		{
			return false;
		}
		else
		{
			cur = cur->child[d];
		}
	}
	return true;
}

int main()
{
	int t;
	cin >> t;
	while (t-- > 0)
	{
		int n;
		cin >> n;
		string s;
		Trie tree;
		bool is_exist = false;
		for (int i = 0; i < n; ++i)
		{
			cin >> s;
			if (!is_exist && !tree.search(s))
			{
				tree.insert(s);
			}
			else
			{
				is_exist = true;
			}
		}
		cout << (is_exist ? "NO" : "YES") << endl;
	}
}



