// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn pseudo_palindromic_paths(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, mask: i32) -> i32 {
            if let Some(n) = node {
                let n = n.borrow();
                
                let new_mask = mask ^ (1 << n.val);

                if n.left.is_none() && n.right.is_none() {
                    if new_mask & (new_mask - 1) == 0 {
                        return 1;
                    } else {
                        return 0;
                    }
                }

                return dfs(n.left.clone(), new_mask) +
                       dfs(n.right.clone(), new_mask);
            }
            0
        }

        dfs(root, 0)
    }
}