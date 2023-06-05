class Solution {
    public void rotate(int[] nums, int k) {
        int length = nums.length;
        int rot = k % length;

        reverse(nums, 0, length - 1);
        reverse(nums, 0, rot - 1); 
        reverse(nums, rot, length - 1); 
    }

    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
}
