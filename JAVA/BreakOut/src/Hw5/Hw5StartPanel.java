package Hw5;

import java.awt.Color;
import java.awt.Font;
import java.awt.FontMetrics;
import java.awt.GradientPaint;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.net.URL;

import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.swing.JPanel;

class Hw5StartPanel extends JPanel implements Runnable{
	Clip startClip;
	int timer = 0;

	Hw5StartPanel() {
		super();
		try {
			URL url = this.getClass().getResource("gameStart.wav");
			AudioInputStream audio = AudioSystem.getAudioInputStream(url);
			startClip = AudioSystem.getClip();
			startClip.open(audio);
		} catch (Exception e) {
			e.printStackTrace();
		}

		startClip.setFramePosition(0);
		startClip.start();
		
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

		Font font = new Font("Algerian", Font.PLAIN, 50);
		FontMetrics metrics = g.getFontMetrics(font);

		g2.setFont(font);
		g2.setColor(Color.WHITE);
		String str = "Java Programming";
		g2.drawString(str, w / 2 - metrics.stringWidth(str) / 2, h / 5);
		str = "HomeWork5";
		g2.drawString(str, w / 2 - metrics.stringWidth(str) / 2, h / 5 + metrics.getAscent());

		font = new Font("Algerian", Font.PLAIN, 80);
		metrics = g.getFontMetrics(font);
		g2.setFont(font);

		str = "block breaker";
		g2.setColor(Color.WHITE);
		g2.drawString(str, w / 2 - metrics.stringWidth(str) / 2, h / 2);

		font = new Font("Impact", Font.PLAIN, 50);
		metrics = g.getFontMetrics(font);
		g2.setFont(font);

		if (timer % 2 == 0) {
			str = "PRESS SAPCE TO GAME START";
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
