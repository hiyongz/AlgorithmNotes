public class addTwoNumbers {
    public static void main(String[] args){
        int[] l1 = {2,4,8};
        int[] l2 = {5,6,1};
        ListNode ListNode1 = CreatListNode(l1);
        ListNode ListNode2 = CreatListNode(l2);
        print(ListNode1); //打印输出
        print(ListNode2); //打印输出
        ListNode res = solution(ListNode1, ListNode2);
        print(res);
    }

    private static ListNode solution(ListNode l1, ListNode l2) {
        ListNode head = null, tail = null;
        int carry = 0;
        while (l1 != null || l2 != null) {
            int n1 = l1 != null ? l1.val : 0;
            int n2 = l2 != null ? l2.val : 0;
            int sum = n1 + n2 + carry;
            if (head == null) {
                head = tail = new ListNode(sum % 10);
            } else {
                tail.next = new ListNode(sum % 10);
                tail = tail.next;
            }
            carry = sum / 10;
            if (l1 != null) {
                l1 = l1.next;
            }
            if (l2 != null) {
                l2 = l2.next;
            }
        }
        if (carry > 0) {
            tail.next = new ListNode(carry);
        }
        return head;
    }

    private static ListNode CreatListNode(int[] list) {
        ListNode head = new ListNode(0);    //创建首节点
        ListNode nextNode;                     //声明一个变量用来在移动过程中指向当前节点
        nextNode=head;                      //指向首节点
        //创建链表
        for (int value : list) {
            nextNode.next = new ListNode(value);               //把心节点连起来
            nextNode = nextNode.next;           //当前节点往后移动
        } //当for循环完成之后 nextNode指向最后一个节点

        nextNode=head;                     //重新赋值让它指向首节点
        return nextNode;
    }

    //Definition for singly-linked list.
    public static class ListNode {
        int val;
        ListNode next;
        ListNode() {
        }
        ListNode(int val) {
            this.val = val;
        }
        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    //打印输出方法
    private static void print(ListNode listNoed){
        //创建链表节点
        while(listNoed!=null){
            System.out.println("节点:"+listNoed.val);
            listNoed=listNoed.next;
        }
        System.out.println();
    }
}