#Question 30 : Word Search II
class Solution:
    #dfs search
    def dfs(self,row,col,visited,board,rootNode,string,result):
        if((row,col) in visited):
            return
        
        elif((row<0 or row>len(board)-1) or (col<0 or col>len(board[0])-1)):
            return 
        
        character = board[row][col]
        if(character not in rootNode.children):
            return
        
        elif(rootNode.children[character].endofword == True):
            result.add(string+character)
        
        visited.add((row,col))
        self.dfs(row+1,col,visited,board,rootNode.children[character],string+character,result)
        self.dfs(row,col+1,visited,board,rootNode.children[character],string+character,result)
        self.dfs(row-1,col,visited,board,rootNode.children[character],string+character,result)
        self.dfs(row,col-1,visited,board,rootNode.children[character],string+character,result)
        visited.remove((row,col))
      
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = set()
        trie = Trie()
        #construct trie from given words
        for word in words:
            trie.addword(word)
        #get root of trie   
        rootNode = trie.getrootNode()
        
        #search words in matrix using trie and dfs
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                visited = set()
                self.dfs(i,j,visited,board,rootNode,"",result)
        
        return list(result)

#trie node
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

#trie Data structures
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def getrootNode(self):
        return self.root
    
    def addword(self,word: str) -> None:
        currNode = self.root
        for i in range(0,len(word)):
            if(word[i] not in currNode.children):
                currNode.children[word[i]] = TrieNode()
            
            currNode = currNode.children[word[i]]
        
        currNode.endofword = True