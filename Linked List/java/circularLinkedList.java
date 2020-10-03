import java.util.Scanner;

class Node{
    int data;
    Node next;
    public Node(int data){
        this.data = data;
    }
}

public class Main {

    public int size =0;
    public Node head=null;
    public Node tail=null;



    
    public void addNodeAtStart(int data){
        System.out.println("Adding node " + data + " at start");
        Node n = new Node(data);
        if(size==0){
            head = n;
            tail = n;
            n.next = head;
        }else{
            Node temp = head;
            n.next = temp;
            head = n;
            tail.next = head;
        }
        size++;
    }

    public void addNodeAtEnd(int data){
        if(size==0){
            addNodeAtStart(data);
        }else{
            Node n = new Node(data);
            tail.next =n;
            tail=n;
            tail.next = head;
            size++;
        }
        System.out.println("\nNode " + data + " is added at the end of the list");
    }

    public void deleteNodeFromStart(){
        if(size==0){
            System.out.println("\nList is Empty");
        }else{
            System.out.println("\ndeleting node " + head.data + " from start");
            head = head.next;
            tail.next=head;
            size--;
        }
    }

    public int elementAt(int index){
        if(index>size){
            return -1;
        }
        Node n = head;
        while(index-1!=0){
            n=n.next;
            index--;
        }
        return n.data;
    }

    
    public void print(){
        System.out.print("Circular Linked List:");
        Node temp = head;
        if(size<=0){
            System.out.print("List is empty");
        }else{
            do {
                System.out.print(" " + temp.data);
                temp = temp.next;
            }
            while(temp!=head);
        }
        System.out.println();
    }


    public int findSize(){
        return size;
    }

    public static void main(String[] args) {
        Main c = new Main();
        Scanner sc=new Scanner(System.in);
        int s=1;
        while(s==1)
        {
            System.out.println("Choose the operation you want to perform");
            System.out.println("Enter 1 to insert an element in the beginning");
            System.out.println("Enter 2 to insert an element at the end");
            System.out.println("Enter 3 to delete an element from the beginning");
            int flag =sc.nextInt();
            switch (flag) 
            {
                case 1:
                    System.out.println("Enter the element");
                    int z=sc.nextInt();
                    c.addNodeAtStart(z);
                    System.out.println("The new List is");
                    c.print();
                    break;
                case 2:
                    System.out.println("Enter the element");
                    int number=sc.nextInt();
                    c.addNodeAtEnd(number);
                    System.out.println("The new List is");
                    c.print();   
                case 3:
                    c.deleteNodeFromStart();
                    System.out.println("The new List is");
                    c.print();
                default:
                    break;
            } 
            System.out.println("Press 1 to Continue");
            s=sc.nextInt();

        }
        System.out.println("Size of linked list: "+ c.findSize());
        
    }

}
