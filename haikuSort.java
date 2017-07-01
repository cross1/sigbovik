import java.util.*;
import java.System.out.*;

public int[] listOfNums = new int[10]

class haiku{
  public static void main(String[] args){
    makeList();
    System.out.println(Arrays.toString(list));
    haiku()
  }

  //method is a haiku
  public void haiku() {      //Public void haiku
    Arrays.sort(listOfNums); //Arrays dot sort list of nums
    println(listOfNums)      //print line list of nums
  }


  private static void makeList() {
    Random random = new Random();
    for(int i = 0; i < listLength; i++) {
      list[i] = random.nextInt(1000);
    }
  }
}
