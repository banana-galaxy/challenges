public static int lateRide(int n){
        int hh = (int) n / 60;
        int mm = n - 60*hh;
        return digitsSum(hh) + digitsSum(mm);
    }

    public static int digitsSum(int n){
        int sum = 0;
        while(n > 0){
            sum += n % 10;
            n = n / 10;
        }
        return sum;
    }