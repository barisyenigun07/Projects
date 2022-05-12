package MineSweeperProject;

import java.util.Random;
import java.util.Arrays;
import java.util.Scanner;

public class MineSweeper {
    private int rowNumber;
    private int columnNumber;
    private String[][] map;
    private int[][] locationMine;
    private int mineNum;
    private boolean isFinished;


    public MineSweeper(int rowNumber, int columnNumber){
        this.rowNumber = rowNumber;
        this.columnNumber = columnNumber;
        this.map = new String[rowNumber][columnNumber];
        this.mineNum = (rowNumber * columnNumber) / 4;
        this.locationMine = new int[mineNum][];
        this.isFinished = false;

    }
    private boolean checkMine(int x, int y){
        int[] controlledLoc = {x,y};
        boolean isMatched = false;
        for (int i = 0;i < this.locationMine.length;i++){
            if (Arrays.compare(this.locationMine[i],controlledLoc) == 0){
                isMatched = true;
                break;
            }
        }
        return isMatched;
    }
    public void specifyMineLocations(){
        Random random = new Random();
        int i = 0;
        while (i < mineNum){
            int xAxis = random.nextInt(rowNumber);
            int yAxis = random.nextInt(columnNumber);
            if (!checkMine(xAxis,yAxis)){
                int[] loc = {xAxis,yAxis};
                this.locationMine[i] = loc;
                i++;
            }
        }

    }

    public void initializeMap(){
        for (int i = 0;i < rowNumber;i++){
            for (int j = 0;j < columnNumber;j++){
                this.map[i][j] = "_";
            }
        }
    }
    public void select(int x, int y){

        if ((x < 0 || x >= rowNumber) || (y < 0 || y >= columnNumber)){
            System.out.println("Incorrect Selection!");
        }
        else{
            if (checkMine(x,y)){
                System.out.println("You selected the mine area! You lost!!!");
                this.map[x][y] = "*";
                isFinished = true;
            }
            else if (!this.map[x][y].equals("_")){
                System.out.println("You entered this location!");
            }
            else{
                int mineNearby = 0;

                int right = x + 1;
                int left = x - 1;
                int up = y - 1;
                int down = y + 1;

                if (right < rowNumber && checkMine(right,y)){
                    mineNearby++;
                }
                if (left >= 0 && checkMine(left,y)){
                    mineNearby++;
                }
                if (up >= 0 && checkMine(x,up)){
                    mineNearby++;
                }
                if (down < columnNumber && checkMine(x,down)){
                    mineNearby++;
                }
                if ((right < rowNumber && up >= 0) && checkMine(right,up)){
                    mineNearby++;
                }
                if ((right < rowNumber && down < columnNumber) && checkMine(right,down)){
                    mineNearby++;
                }
                if ((left >= 0 && up >= 0) && checkMine(left,up)){
                    mineNearby++;
                }
                if ((left >= 0 && down < columnNumber) && checkMine(left,down)){
                    mineNearby++;
                }
                this.map[x][y] = String.valueOf(mineNearby);
                
            }
        }
    }

    public void checkFinished(){
        boolean underscoreFound = false;
        for (int i = 0;i < rowNumber;i++){
            for (int j = 0;j < columnNumber;j++){
                if (this.map[i][j].equals("_")){
                    underscoreFound = true;
                    break;
                }
            }
        }
        if (!underscoreFound){
            System.out.println("Congratulations! You won!!!");
            isFinished = true;
        }
    }

    public void printMap(){
        for (int i = 0;i < rowNumber;i++){
            for (int j = 0;j < columnNumber;j++){
                System.out.print(this.map[i][j] + " ");
            }
            System.out.println();
        }
    }



    public void run(){
        initializeMap();
        specifyMineLocations();
        while (!isFinished){
            printMap();
            Scanner scanner = new Scanner(System.in);
            System.out.print("Enter xAxis:");
            int x = scanner.nextInt();
            System.out.print("Enter yAxis:");
            int y = scanner.nextInt();
            select(x,y);
            checkFinished();
        }
        printMap();
    }
}
