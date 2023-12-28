import scala.annotation.tailrec

object Solution {
    @tailrec def canJump(nums: Array[Int]): Boolean = {
        if (nums.length <= 1) true else {
            nums(0) match {
                case 0 => false
                case jmp if jmp >= (nums.length - 1) => true
                case jmp => {
                    var indMax = 0
                    var jmpDistMax = 0

                    for (i <- Range(1, jmp + 1)) {
                        val dist = i + nums(i)

                        if (dist > jmpDistMax) {
                            jmpDistMax = dist
                            indMax = i
                        }
                    } 

                    Solution.canJump(nums.slice(indMax, nums.length)) 
                }
            }
        }
    }
}
