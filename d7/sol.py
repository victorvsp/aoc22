'''
PS: I am certainly going a bit overboard. Better spend 10 minutes solving this right than more time later debugging very bad code.
'''

import math

class FileNode:
    def __init__(self, size, name):
        self.size = size
        self.name = name

class DirNode:
    root_dir = None

    def __init__(self, parent_dir, name):
        self.parent_dir = parent_dir
        self.content_dict = {"." : self, ".." : parent_dir, "/" : DirNode.root_dir}
        self.name = name
        self.size = -1 # To be computed later
    
    def getRootDir():
        if DirNode.root_dir is None:
            DirNode.root_dir = DirNode(None,"/")
            DirNode.root_dir.parent_dir = DirNode.root_dir
            DirNode.root_dir.content_dict[".."] = DirNode.root_dir
            DirNode.root_dir.content_dict["/"] = DirNode.root_dir
        return DirNode.root_dir
    
    # Return total size and sum of sizes of dirs (counting itself) with size <= MAX_SIZE
    def countTotalSize(self, MAX_SIZE = 100000):

        self_size = 0
        dir_size_sum = 0

        for item_name in self.content_dict:
            if item_name in [".", "..", "/"]:
                continue

            item = self.content_dict[item_name]
            if isinstance(item, DirNode):
                (subdir_size, subdir_size_sum) = item.countTotalSize()
                self_size += subdir_size 
                dir_size_sum += subdir_size_sum
            else:
                self_size += item.size
        
        if self_size <= MAX_SIZE:
            dir_size_sum += self_size
        
        self.size = self_size
        return (self_size, dir_size_sum)

        
    # Assumes weights were computed before
    def smallestDirSizeToDelete(self, required_size):

        smallest_size_to_delete = math.inf

        for item_name in self.content_dict:
            if item_name in [".", "..", "/"]:
                continue

            item = self.content_dict[item_name]
            if isinstance(item, DirNode):
                smallest_size_subdir = item.smallestDirSizeToDelete(required_size)
                smallest_size_to_delete = min(smallest_size_to_delete,
                                                smallest_size_subdir)
           
        if self.size >= required_size:
            smallest_size_to_delete = min(smallest_size_to_delete,
                                            self.size)
        return smallest_size_to_delete


def executeOneCommand(current_line_list, init_dir):
    current_dir = init_dir
    cmd = current_line_list[0].strip().split()
    lines_read = 1
    #print("[?????] {}".format(cmd))
    if cmd[0] != "$":
        print("[!!!] Unexpected line: {}".format(current_line_list[0]))
        return (current_line_list[lines_read:], current_dir)
    
    if cmd[1] == "cd":
        dir_name = cmd[2]
        if dir_name in current_dir.content_dict:
            current_dir = current_dir.content_dict[dir_name]
        else:
            print("[!!!] cd into unknown dir")
            current_dir = DirNode(current_dir, dir_name)
            
    elif cmd[1] == "ls":
        while lines_read < len(current_line_list) and current_line_list[lines_read][0] != "$":
            (item_info, item_name) = current_line_list[lines_read].split()
            
            if not (item_name in current_dir.content_dict):
                if item_info == "dir":
                    current_dir.content_dict[item_name] = DirNode(current_dir, item_name)
                else:
                    item_size = int(item_info)
                    current_dir.content_dict[item_name] = FileNode(item_size, item_name)


            lines_read += 1
    else:
        print("[!!!] Command not recognized: {}".format(current_line_list[0]))

    return current_line_list[lines_read:], current_dir

def solutionPartOne():
    (_, result) = DirNode.root_dir.countTotalSize()
    print(result)

def solutionPartTwo():
    total_size = 70000000
    total_space_needed = 30000000
    (used_space, _) = DirNode.root_dir.countTotalSize()
    space_to_free = total_space_needed - (total_size - used_space)
    result = DirNode.root_dir.smallestDirSizeToDelete(space_to_free)
    print(result)


##### Main #####

input_f = open("input.txt","r")
line_list = input_f.readlines()
current_line_list = line_list
current_dir = DirNode.getRootDir()

while len(current_line_list) > 0:
    (current_line_list, current_dir) = executeOneCommand(current_line_list,
                                                         current_dir)
solutionPartOne()
solutionPartTwo()                                                