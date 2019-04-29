import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Point;
import java.awt.event.MouseEvent;
import java.awt.event.MouseMotionAdapter;
import java.awt.event.MouseWheelEvent;
import java.awt.event.MouseWheelListener;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.net.URL;

import javax.imageio.ImageIO;
import javax.swing.JFrame;
import javax.swing.JPanel;

class P10 extends JPanel {

	Point p = new Point();
	int size = 100;

	BufferedImage img;

	public P10() {

		try {
			URL url = this.getClass().getResource("lena.jpg");
			img = ImageIO.read(url);
		} catch (IOException e) {
			e.printStackTrace();
		}

		addMouseMotionListener(new MouseMotionAdapter() {
			@Override
			public void mouseMoved(MouseEvent e) {
				p = e.getPoint();
				repaint();
			}

			@Override
			public void mouseDragged(MouseEvent e) {
				p = e.getPoint();
				repaint();
			}
		});

		addMouseWheelListener(new MouseWheelListener() {
			@Override
			public void mouseWheelMoved(MouseWheelEvent e) {
				// TODO Auto-generated method stub
				int rot = e.getWheelRotation();
				size += rot * 5;
				if (size < 10)
					size = 10;
				repaint();

			}
		});

	}

	@Override
	protected void paintComponent(Graphics g) {
		super.paintComponent(g);

		g.drawImage(img, 0, 0, null);

		int w = img.getWidth();
		int h = img.getHeight();

		int x = p.x - size / 2;
		if (x < 0)
			x = 0;
		if (x > img.getWidth() - size)
			x = img.getWidth() - size;
		int y = p.y - size / 2;
		if (y < 0)
			y = 0;
		if (y > img.getHeight() - size)
			y = img.getHeight() - size;

		g.setColor(Color.red);
		g.drawRect(x, y, size, size);

		g.drawImage(img, w, 0, w + 300, 300, x, y, x + size, y + size, null);

	}
}

public class Exam10 extends JFrame {

	public Exam10() {
		this.setSize(1000, 1000);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);

		P10 p = new P10();
		add(p);

		this.setVisible(true);
	}

	public static void main(String[] args) {
		new Exam10();
	}

}
