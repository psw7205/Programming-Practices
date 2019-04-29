import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Point;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

class blinkingJLabel extends JLabel {

	blinkingJLabel(String str, int interval) {
		super(str);
		this.setOpaque(true);
		blinkingJLabel l = this;

		Thread t = new Thread(new Runnable() {
			@Override
			public void run() {

				int i = 0;
	
				while (true) {
					i++;
					if (i % 2 == 0)
						l.setBackground(Color.BLUE);
					else
						l.setBackground(Color.YELLOW);

					try {
						Thread.sleep(interval);
					} catch (InterruptedException e) {
						e.printStackTrace();
						return;
					}
				}
			}

		});
		
		t.start();
	}
}

class ThreadPanel extends JPanel implements Runnable {
	int time;
	Thread t;
	Point pt;

	ThreadPanel() {
		pt = new Point(200, 200);

		blinkingJLabel l1 = new blinkingJLabel("±ôºý", 1000);
		add(l1);
		JLabel l2 = new JLabel("===");
		add(l2);
		blinkingJLabel l3 = new blinkingJLabel("±ôºý±ôºý", 100);
		add(l3);

		ThreadPanel p = this;
		JLabel label = new JLabel();
		add(label);

		t = new Thread(this);
		t.start();

		JButton btn = new JButton("STOP");
		btn.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				t.interrupt();
			}
		});

		JButton btn2 = new JButton("RESTART");
		btn2.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				if (t.isAlive() != true) {
					t = new Thread(p);
					t.start();
				}
			}
		});

		add(btn);
		add(btn2);

//		ThreadPanel p = this;
//		JButton button = new JButton("btn");
//		add(button);
//		button.addActionListener(new ActionListener() {
//			@Override
//			public void actionPerformed(ActionEvent e) {
//				for (int i = 0; i < 100000; i++) {
//					time = i;
//					p.repaint();
//				}
//			}
//		}); // ÇÑ¹ø¿¡ ½ÇÇàµÇ±â¿¡ ½ÇÆÐ

	}

	@Override
	protected void paintComponent(Graphics g) {
		super.paintComponent(g);

		String str = "" + time;
		g.setFont(new Font("Arial", Font.PLAIN, 50));
		g.drawString(str, 100, 100);

		g.drawRect(pt.x, pt.y, 100, 100);
		g.drawString("" + Thread.activeCount(), 100, 150);
	}

	int dx = 10;

	@Override
	public void run() {

		while (true) {
			time++;
			pt.x += dx;

			if (pt.x + 100 > this.getWidth()) {
				pt.x = this.getWidth() - 100;
				dx = -dx;

			} else if (pt.x < 0) {
				pt.x = 0;
				dx = -dx;
			}

			try {
				Thread.sleep(30);
			} catch (InterruptedException e) {
				e.printStackTrace();
				return;
			}

			repaint();
		}
	}
}

public class ThreadPractice extends JFrame {
	ThreadPractice() {
		setSize(500, 500);
		setTitle("Thread Practice");
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		add(new ThreadPanel());

		this.setVisible(true);
	}

	public static void main(String[] args) {
		new ThreadPractice();
	}

}
