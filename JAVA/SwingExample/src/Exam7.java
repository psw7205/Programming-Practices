import java.awt.Font;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

class P7 extends JPanel implements Runnable, ActionListener {

	int t;
	int h, m, s;

	JButton btn1, btn2, btn3;

	P7() {

		btn1 = new JButton("HOUR");
		btn2 = new JButton("MIN");
		btn3 = new JButton("SEC");

		btn1.addActionListener(this);
		btn2.addActionListener(this);
		btn3.addActionListener(this);

		add(btn1);
		add(btn2);
		add(btn3);

		Thread t = new Thread(this);

		t.start();

	}

	@Override
	public void actionPerformed(ActionEvent e) {
		if (e.getSource() == btn1)
			t += 3600;
		if (e.getSource() == btn2)
			t += 60;
		if (e.getSource() == btn3)
			t += 1;

		repaint();
	}

	@Override
	protected void paintComponent(Graphics g) {
		super.paintComponent(g);
		h = t / 60 / 60 % 60;
		m = t / 60 % 60;
		s = t % 60;

		String str = new String();

		if (h < 10)
			str += "0";
		str += h + ":";

		if (m < 10)
			str += "0";
		str += m + ":";

		if (s < 10)
			str += "0";
		str += s + "";

		g.setFont(new Font("Arial", Font.BOLD, 100));
		g.drawString(str, 10, getSize().height / 2);
	}

	@Override
	public void run() {
		while (true) {
			try {
				Thread.sleep(1000);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}

			t++;
			repaint();
		}
	}
}

public class Exam7 extends JFrame {
	Exam7() {
		setSize(500, 500);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		P7 p = new P7();
		add(p);
		setVisible(true);
	}

	public static void main(String[] args) {

		new Exam7();
	}
}
