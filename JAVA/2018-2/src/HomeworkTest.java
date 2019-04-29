import java.awt.Graphics;
import java.util.LinkedList;

import javax.swing.JFrame;
import javax.swing.JPanel;

class MyObject{
	void draw(Graphics g){};
	void update(double dt){};
	void resolveCollision(MyObject o){};
}
class MyBlock extends MyObject{
	int x, y, w, h;
	MyBlock(int _x, int _y, int _w, int _h)
	{
		x = _x;
		y = _y;
		w = _w;
		h = _h;
	}
	void draw(Graphics g)
	{
		g.drawRect(x, y,  w,  h);
	}	
}

class MyBall extends MyObject
{
	double x, y, r;
	double vx, vy;
	double prex, prey;
	MyBall()
	{
		x = Math.random()*300 + 100;
		y = Math.random()*300 + 100;
		r = 5;
		vx = Math.random()*200-100;
		vy = Math.random()*200-100;
	}
	void draw(Graphics g)
	{
		g.fillOval((int)(x-r),  (int)(y-r), (int)(2*r), (int)(2*r));
	}
	@Override void update(double dt)
	{
		prex = x;
		prey = y;
		x += vx*dt;
		y += vy*dt;
	}
	@Override void resolveCollision(MyObject o)
	{
		if(o instanceof MyBlock)
		{
			MyBlock b = (MyBlock) o;
			double x1 = b.x - r;
			double y1 = b.y - r;
			double x2 = b.x + b.w + r;
			double y2 = b.y + b.h + r;
			if(x>x1 && x<x2 && y>y1 && y<y2)
			{
				if(prey<y1) { y = y1; vy = -vy; }
				if(prey>y2) { y = y2; vy = -vy; }
				if(prex<x1) { x = x1; vx = -vx; }
				if(prex>x2) { x = x2; vx = -vx; }
			}
			
		}
	}
}

class GamePanel extends JPanel implements Runnable
{
	LinkedList<MyObject> obj = new LinkedList<MyObject>();
	GamePanel()
	{
		obj.add(new MyBlock(0,0,500,20));
		obj.add(new MyBlock(0,440,500,20));
		obj.add(new MyBlock(0,0,20,500));
		obj.add(new MyBlock(460,0,20,500));	
		
		obj.add(new MyBlock(300,200,100,200));
		
		for(int i=0; i<40; i++)
			obj.add(new MyBall());
		
		Thread t = new Thread(this);
		t.start();
		
	}
	@Override protected void paintComponent(Graphics g)
	{
		super.paintComponent(g);
		for(MyObject o : obj)
			o.draw(g);
	}
	@Override
	public void run() {
		while(true)
		{
			double dt = 0.033;
			try {
				Thread.sleep((int)(dt*1000));
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			for(MyObject o: obj)
				o.update(dt);
			
			for(MyObject o: obj)
				if(o instanceof MyBall)
					for(MyObject b: obj)
						o.resolveCollision(b);
			
			repaint();
		}
		
	}
	
}

public class HomeworkTest extends JFrame{
	HomeworkTest()
	{
		setSize(500,500);
		setTitle("...");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	
		GamePanel p = new GamePanel();
		add(p);
		
		
		setVisible(true);		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new HomeworkTest();
	}

}