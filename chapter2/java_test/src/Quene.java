/**
 * Created by zhangchao on 2015/5/8.
 */
public class Quene {

    private int maxSize ;
    private long[] queArray ; //队列

    private int front ; //队头
    private int rear ; //队尾
    private int nItems ; //元素个数

    public Quene(int s){
        maxSize = s ;
        queArray = new long[maxSize] ;
        front = 0 ;
        rear = -1 ;
        nItems = 0 ;
    }

    public void insert(long j){ //进队列

        if(rear == maxSize-1)
            rear = -1 ;
        queArray[++rear] = j;
        nItems++;
    }

    public long remove(){   //取得队列的队头元素
        long temp = queArray[front++]; //取值和修改队列指针
        if (front == maxSize) // 处理循环
            front = 0 ;
        nItems--;
        return temp;
    }

    public long peekFront(){
        return queArray[front];
    }

    public boolean isEmpty(){
        return (nItems==0);
    }

    public boolean isFull(){
        return (rear == maxSize);
    }

    public int size() {
        return nItems;

    }

    public static void main(String[] args){
        System.out.print("hello world");
    }

}
