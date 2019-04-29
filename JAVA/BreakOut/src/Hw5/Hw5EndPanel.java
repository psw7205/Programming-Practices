package Hw5;

import java.awt.Color;
import java.awt.Font;
import java.awt.FontMetrics;
import java.awt.GradientPaint;
import java.awt.Graphics;
import java.awt.Graphics2D;

import javax.swing.JPanel;

class Hw5EndPanel extends JPanel implements Runnable{
	int timer = 0;
	int score = 0;
	
	public Hw5EndPanel() {
		
		Thread t = new Thread(this);
		t.start();
	}

	protected void paintComponent(Graphics g) {
		super.paintComponent(g);

		int w = getWidth();
		int h = getHeight();

		Graphics2D g2 = (Graphics2D) g;
		g2.setPaint(new GradientPaint(0.0f, 0.0f, Color.darkGray, 0.0f, h, Color.gray));
		g2.fillRect(0, 0, w, h);

		Font font = new Font("Algerian", Font.PLAIN, 110);
		FontMetrics metrics = g.getFontMetrics(font);
		g2.setFont(font);

		String str = "GAME OVER";

		g2.setColor(Color.WHITE);
		g2.drawString(str, w / 2 - metrics.stringWidth(str) / 2, h / 3);
		
		
		font = new Font("Impact", Font.PLAIN, 50);
		metrics = g.getFontMetrics(font);
		g2.setFont(font);
		str = "SCORE : " + score;
		
		g2.drawString(str, w / 2 - metrics.stringWidth(str) / 2 + 1, h / 5 * 3 + 1);
		g2.setColor(Color.BLACK);
		g2.drawString(str, w / 2 - metrics.stringWidth(str) / 2, h / 5 * 3);
		
		
		font = new Font("Impact", Font.PLAIN, 50);
		metrics = g.getFontMetrics(font);
		g2.setFont(font);

		if (timer % 2 == 0) {
			str = "PRESS SAPCE";
			g2.setColor(Color.black);
			g2.drawString(str, w / 2 - metrics.stringWidth(str) / 2 + 2, 602);
			g2.setColor(Color.RED);
			g2.drawString(str, w / 2 - metrics.stringWidth(str) / 2, 600);

		}
		
	}

	@Override
	public void run() {
		while(true)
		{
			try {
				Thread.sleep(500);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
			timer++;
			repaint();
		}
	}
}
