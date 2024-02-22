class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int maxHealth = health;
        int endTime = attacks[attacks.length-1][0];
        int health_cnt = 0;
        int cnt = 0;
        for(int i=0; i<=endTime; i++) {
            if (i == attacks[cnt][0]) {
                health -= attacks[cnt][1];
                if (health <= 0) return -1;
                health_cnt = 0;
                cnt++;
            } else {
                health += bandage[1];
                health_cnt++;
                if (health_cnt == bandage[0]) {
                    health += bandage[2];
                    health_cnt = 0;
                }
                health = Math.min(health, maxHealth);
            }
        }
        
        return health;
    }
}