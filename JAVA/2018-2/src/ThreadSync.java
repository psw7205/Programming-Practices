import java.util.ArrayList;

class SharedData {
	int sum = 0;

	// critical section : 계산을 하는 동안 아무도 수정 못하게 막아야함 -> Lock, Unlock을 통해 해결
	// Synchronization : 동기화를 통해 해결
	synchronized public void add() {
		// 함수전체, 특정부분만 묶기 가능, 다만 쓰레드의 의미가 사라짐
		synchronized (this) {
			int n = sum;
			n += 10;

			// System.out.print(Thread.currentThread().getName());
			// System.out.println(" Sum : " + n);

			try {
				Thread.sleep((int) (Math.random() * 10));
			} catch (InterruptedException e) {
				e.printStackTrace();
			}

			sum = n;
		}
		
		System.out.print(Thread.currentThread().getName());
		System.out.println(" Sum : " + sum); // 데이터가 공유되기에 수정되기 전에 다른 곳에서 쓰면 값이 이상해짐
	}
}

class MyAddingThread extends Thread {
	SharedData d;

	MyAddingThread(String name, SharedData in) {
		super(name);
		d = in;
	}

	@Override
	public void run() {
		for (int i = 0; i < 100; i++)
			d.add();
	}
}

public class ThreadSync {

	public static void main(String[] args) {
		SharedData d = new SharedData();

		System.out.println(Thread.currentThread().getName());

		MyAddingThread t = new MyAddingThread("A", d);
		MyAddingThread t2 = new MyAddingThread("B", d);
		MyAddingThread t3 = new MyAddingThread("C", d);
		MyAddingThread t4 = new MyAddingThread("D", d);
		t.start();
		t2.start();
		t3.start();
		t4.start();
		
	}

}
