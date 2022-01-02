import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class twoSum {

    public static void main(String[] args){
        int[] nums = {1, 7, 11, -2,15};
        // int[] res = Solution(nums,9);
        int[] res2 = twoSum2(nums,9);
        System.out.println(
                Arrays.toString(res2));

    }

    public static int[] Solution(int[] nums, int target) {
        int[] index = new int[2];
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    index[0] = i;
                    index[1] = j;
                    return index;
                }
            }
        }
        return new int[0];
    }

    public static int[] twoSum2(int[] nums, int target) {
        Map<Integer, Integer> hashtable = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; ++i) {
            if (hashtable.containsKey(nums[i])) {
                return new int[]{hashtable.get(nums[i]), i};
            }
            hashtable.put(target - nums[i], i);
        }
        return new int[0];
    }
}