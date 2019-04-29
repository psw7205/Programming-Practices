import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.JFrame;
import javax.swing.JPanel;

class ImagePracticePanel extends JPanel {

	BufferedImage img;

	ImagePracticePanel() {
		try {
			img = ImageIO.read(new File("1.png"));
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	@Override
	protected void paintComponent(Graphics g) {
		super.paintComponent(g);
		// g.drawImage(img,20,20, null); // 20, 20 좌표에서 이미지 그림
		// g.drawImage(img, 100, 100, 100, 100, null); // 100,100좌표에서 200 200 크기만큼 그림
		// g.drawImage(img, 0, 0, getWidth(), getHeight(), null); // 화면 가득 채우기
		// g.drawImage(img, 100, 100, 300, 300, 0, 0, 200, 200, null); // 이미지의 0,0 ~
		// 400,400 만큼 잘라 그리기

		int divX = 4;
		int divY = 4;
		int dw = img.getWidth() / divX;
		int dh = img.getHeight() / divY;
		int offset = 10;
		int num = divX * divY;
		int idx[] = new int[num];

		int drawIdx = 0;
		for (int i = 0; i < num; i++)
			idx[i] = i;

		for (int i = 0; i < num; i++) {
			int j = (int) (Math.random() * num);
			int tmp = idx[j];
			idx[j] = idx[i];
			idx[i] = tmp;
		}

		for (int i = 0; i < divX; i++) {
			for (int j = 0; j < divY; j++) {
				int dx = (dw + offset) * i;
				int dy = (dh + offset) * j;
				int sx = dw * (idx[drawIdx] / divY);
				int sy = dh * (idx[drawIdx] % divY);

				g.drawImage(img, dx, dy, dx + dw, dy + dh, sx, sy, sx + dw, sy + dh, null);

				drawIdx++;
			}
		}

	}
}

class MyThread extends Thread {
	String name;

	@Override
	public void run() {
		for (int i = 0; i < 100; i++) {
			System.out.println(name + i);
			for (int j = 0; j < 10000000; j++)
				; // 작업량을 늘려 멀티스레딩을 확실히 보기위한 반복문

		}
	}
}

public class ImagePractice extends JFrame implements Runnable {

	ImagePractice() {
		setTitle("Image Practic");
		setSize(700, 700);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		ImagePracticePanel p = new ImagePracticePanel();
		add(p);

		setVisible(true);
	}

	public static void main(String[] args) {
		ImagePractice f = new ImagePractice();

		MyThread t1 = new MyThread();
		t1.name = "t1 : ";

		MyThread t2 = new MyThread();
		t2.name = "t2 : ";

		Thread t3 = new Thread(f); // Runnable 인터페이스 구현
		Thread t4 = new Thread(new Runnable(){
			@Override
			public void run() {
				// 내용
			}
		});
		
		t1.start(); // 작업자를 구해와서 일을 시킴
		t2.start(); // run()를 직접 부르는 건 안됨, 메인에서 함수호출하는 것이기에 멀티쓰레딩 X
		t3.start();
		t4.start();
	}

	@Override
	public void run() {
		for (int i = 0; i < 100; i++) {
			System.out.println("t3 : " + i);
			for (int j = 0; j < 10000000; j++)
				;
		}

	}
}
