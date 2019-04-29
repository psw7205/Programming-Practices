import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.net.URL;

import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

class AudioPanel extends JPanel implements ActionListener {

	Clip clip; // 음악파일 하나

	AudioPanel() {
		try {
			URL url = this.getClass().getResource("loop.wav");
			AudioInputStream audio = AudioSystem.getAudioInputStream(url);
			
				clip = AudioSystem.getClip();
				clip.open(audio);
		}
		 catch (Exception e) { // 파일이 없을경우
			e.printStackTrace();
		}
		
		JButton btn1 = new JButton("play");
		JButton btn2 = new JButton("loop");
		JButton btn3 = new JButton("stop");

		btn1.addActionListener(this);
		btn2.addActionListener(this);
		btn3.addActionListener(this);

		add(btn1);
		add(btn2);
		add(btn3);

	}

	@Override
	public void actionPerformed(ActionEvent arg0) {

		switch (arg0.getActionCommand()) {
		case "play":
			clip.setFramePosition(0); // 음악의 처음으로 이동
			clip.start();
			break;
		case "loop":
			clip.loop(Clip.LOOP_CONTINUOUSLY); // 무한반복
			break;
		case "stop":
			clip.stop();
			break;
		default:
			break;
		}
	}

}

public class AudioTest extends JFrame {

	AudioTest() {
		this.setSize(300, 300);
		this.setTitle("Audio Player");
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		AudioPanel p = new AudioPanel();
		this.add(p);

		this.setVisible(true);
	}

	public static void main(String[] args) {
		new AudioTest();
	}

}
