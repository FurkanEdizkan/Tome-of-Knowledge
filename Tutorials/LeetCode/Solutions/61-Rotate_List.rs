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
    pub fn rotate_right(mut head: Option<Box<ListNode>>, k: i32) -> Option<Box<ListNode>> {
        if head.is_none() {
            return None;
        }

        let mut len = 0;
        let mut curr = &head;
        while let Some(node) = curr {
            len += 1;
            curr = &node.next;
        }

        let k = (k as usize) % len;
        if k == 0 {
            return head;
        }

        let split_at = len - k;
        let mut curr = &mut head;
        for _ in 0..(split_at - 1) {
            curr = &mut curr.as_mut().unwrap().next;
        }

        let mut new_head = curr.as_mut().unwrap().next.take();

        let mut tail = &mut new_head;
        while tail.as_ref().unwrap().next.is_some() {
            tail = &mut tail.as_mut().unwrap().next;
        }
        tail.as_mut().unwrap().next = head;

        new_head
    }
}