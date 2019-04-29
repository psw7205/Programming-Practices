import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JToggleButton;

class P8 extends JPanel implements Runnable, ActionListener {

	int t;
	int h, m, s;

	JToggleButton toggle;
	JButton btn1, btn2, btn3;

	P8() {

		btn1 = new JButton("HOUR");
		btn2 = new JButton("MIN");
		btn3 = new JButton("SEC");
		toggle = new JToggleButton("Digital Clock");
		toggle.addActionListener(this);

		btn1.addActionListener(this);
		btn2.addActionListener(this);
		btn3.addActionListener(this);

		add(btn1);
		add(btn2);
		add(btn3);
		add(toggle);
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

		if (e.getSource() == toggle) {
			if (toggle.isSelected())
				toggle.setText("Round Clock");
			else
				toggle.setText("Digital Clock");
		}

		repaint();
	}

	@Override
	protected void paintComponent(Graphics g) {
		super.paintComponent(g);
		h = t / 60 / 60 % 60;
		m = t / 60 % 60;
		s = t % 60;
		Dimension d = getSize();
		if (toggle.isSelected() == false) {
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
		} else {
			int offset = 50;
			int cx = d.width / 2;
			int cy = d.height / 2 - offset;
			int r = Math.min(cx, cy);
			cy += offset;

			Graphics2D g2 = (Graphics2D) g;
			g2.setStroke(new BasicStroke(2));

			g2.setColor(Color.white);
			g2.fillOval(cx - r, cy - r, 2 * r, 2 * r);
			g2.setColor(Color.black);
			g2.drawOval(cx - r, cy - r, 2 * r, 2 * r);

			double x1, y1, x2, y2;
			double r1, r2;
			double theta;
			for (int i = 0; i < 60; i++) {
				theta = 360.0f / 60.0f * i / 180.0f * 3.141592f;
				r1 = r;
				r2 = r * 0.95;
				if (i % 5 == 0)
					r2 = r * 0.9;
				x1 = r1 * Math.cos(theta) + cx;
				y1 = r1 * Math.sin(theta) + cy;
				x2 = r2 * Math.cos(theta) + cx;
				y2 = r2 * Math.sin(theta) + cy;
				g2.drawLine((int) x1, (int) y1, (int) x2, (int) y2);
			}

			g2.setStroke(new BasicStroke(3));
			g2.setColor(Color.blue);

			theta = s / 60.0 * 3.141592 * 2 - 3.141592 / 2;
			r1 = r * 0.9;
			x1 = r1 * Math.cos(theta) + cx;
			y1 = r1 * Math.sin(theta) + cy;
			g2.drawLine(cx, cy, (int) x1, (int) y1);

			g2.setStroke(new BasicStroke(5));
			g2.setColor(Color.green);

			theta = m / 60.0 * 3.141592 * 2 - 3.141592 / 2;
			r1 = r * 0.7;
			x1 = r1 * Math.cos(theta) + cx;
			y1 = r1 * Math.sin(theta) + cy;
			g2.drawLine(cx, cy, (int) x1, (int) y1);

			g2.setStroke(new BasicStroke(9));
			g2.setColor(Color.red);

			theta = (h % 12 * 60 + m) / (60.0 * 12.0) * 3.141592 * 2 - 3.141592 / 2;
			r1 = r * 0.5;
			x1 = r1 * Math.cos(theta) + cx;
			y1 = r1 * Math.sin(theta) + cy;
			g2.drawLine(cx, cy, (int) x1, (int) y1);

		}

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

public class Exam8 extends JFrame {
	Exam8() {
		setSize(500, 500);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		P8 p = new P8();
		add(p);
		setVisible(true);
	}

	public static void main(String[] args) {

		new Exam8();
	}
}
