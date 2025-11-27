class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        int carry = 0;
        while (l1 != null || l2 != null || carry != 0) {
            int a = (l1 != null) ? l1.val : 0;
            int b = (l2 != null) ? l2.val : 0;
            int sum = a + b + carry;
            carry = sum / 10;
            cur.next = new ListNode(sum % 10);
            cur = cur.next;
            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }
        return dummy.next;
    }

    // helper: build list from array (digits in reverse order as given)
    static ListNode fromArray(int[] a) {
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        for (int v : a) {
            cur.next = new ListNode(v);
            cur = cur.next;
        }
        return dummy.next;
    }

    // helper: print list as [x,y,z]
    static void printList(ListNode node) {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        boolean first = true;
        while (node != null) {
            if (!first) sb.append(",");
            sb.append(node.val);
            first = false;
            node = node.next;
        }
        sb.append("]");
        System.out.println(sb.toString());
    }

    public static void main(String[] args) {
        // Example 1: l1 = [2,4,3], l2 = [5,6,4] -> [7,0,8]
        ListNode l1 = fromArray(new int[]{2,4,3});
        ListNode l2 = fromArray(new int[]{5,6,4});
        printList(addTwoNumbers(l1, l2));

        // Example 2: l1 = [0], l2 = [0] -> [0]
        l1 = fromArray(new int[]{0});
        l2 = fromArray(new int[]{0});
        printList(addTwoNumbers(l1, l2));

        // Example 3: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] -> [8,9,9,9,0,0,0,1]
        l1 = fromArray(new int[]{9,9,9,9,9,9,9});
        l2 = fromArray(new int[]{9,9,9,9});
        printList(addTwoNumbers(l1, l2));
    }
}