// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn swap_pairs(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        // Recursive approach: swap pairs by rearranging nodes
        match head {
            Some(mut node1) => {
                match node1.next {
                    Some(mut node2) => {
                        // Swap: node2 becomes head, node1.next points to recursive result
                        node1.next = Self::swap_pairs(node2.next);
                        node2.next = Some(node1);
                        Some(node2)
                    }
                    None => {
                        // No pair to swap, return as is
                        Some(node1)
                    }
                }
            }
            None => None,
        }
    }
}