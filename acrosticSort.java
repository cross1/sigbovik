import java.util.*;

class acrosticSort{
  public static void main(String[] args){
    int[] list = makeList(10);
    System.out.println(Arrays.toString(list));
    int[] sortedList = acrostic(list);
    System.out.println(Arrays.toString(sortedList));
  }

  public static int[] acrostic(int[] list) {
    int[] ode =  list;
    long haiku = 575;
    long sonnet = 14;
    Arrays.sort(ode);
    return ode;
  }


  private static int[] makeList(int listLength) {
    Random random = new Random();
    int[] list = new int[listLength];
    for(int i = 0; i < listLength; i++) {
      list[i] = random.nextInt(1000);
    }
    return list;
  }
}
