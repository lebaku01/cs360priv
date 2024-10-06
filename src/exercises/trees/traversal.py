#!/usr/bin/env python3
"""
`trees` implementation and driver
Turning in-order and post-order tree traversals into pre-order


@authors:
@version: 2022.9
"""


def get_preorder(inorder: str, postorder: str) -> str:
    """
    Returns pre-order traversal of a tree based on its in-order and post-order traversals

    :param inorder: in-order tree traversal
    :param postorder: post-order tree traversal
    :return: pre-order tree traversal
    >>> get_preorder("UOMELBARTKGSNI", "UMELABORSGNIKT")
    'TROUBLEMAKINGS'
    """
    #grab root, left and right subtrees in both inorder and postorder
    root = postorder[-1]
    inorder_subtrees = inorder.split(postorder[len(postorder) - 1])
    postorder = postorder[:len(postorder) - 1]
    postorder_subtrees = [postorder[0:len(inorder_subtrees[0])],
                          postorder[len(inorder_subtrees[0]):]]
    #base case : two empty subtrees
    if inorder_subtrees[0] == inorder_subtrees[1] == "":
        return root
    #recursive cases, 1) right subtree empty 2) left subtree empty 3) both subtrees non-empty
    elif inorder_subtrees[1] == "":
        return root + get_preorder(inorder_subtrees[0], postorder_subtrees[0])
    elif inorder_subtrees[0] == "":
        return root + get_preorder(inorder_subtrees[1], postorder_subtrees[1])
    else:
        return (root + get_preorder(inorder_subtrees[0], postorder_subtrees[0])
                + get_preorder(inorder_subtrees[1], postorder_subtrees[1]))



def main():
    """This is the main function"""
    print("Pre-order tree traversal")
    print(get_preorder(inorder="UOMELBARTKGSNI", postorder="UMELABORSGNIKT"))


if __name__ == "__main__":
    main()
