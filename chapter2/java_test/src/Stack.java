/**
 * Created by Administrator on 2015/5/8.
 */
import java.util.ArrayList;


public class Stack {
    Object[] data;
    int maxSize;
    int top;

    public Stack(int maxSize){
        this.maxSize = maxSize;
        data = new Object[maxSize];
        top = -1;
    }

    public int getSize(){
        return maxSize;
    }

    public int getElementCount(){
        return top;
    }

    public boolean isEmpty(){
        return top == -1;
    }

    public boolean isFull(){
        return top+1 == maxSize;
    }

    public boolean push(Object data){
        if (isFull()){
            System.out.print("stack is full");
            return false;
        }
        this.data[++top] = data;
        return true;
    }


    public static void  main(String[] args){

        int t = 1;
        int s = 1;
        int k1 = t++;
        int k2 = ++s;
        System.out.print(t+"\n");
        System.out.print(k1+"\n");
        System.out.print(k2+"\n");

        System.out.print("hello world");
    }





}
