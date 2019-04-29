import java.awt.BorderLayout;
import java.awt.Color;

import javax.swing.*;

public class HelloSwing extends JFrame {
// multi thread
// 일반적으로 프로그램 그 자체가 프레임
	HelloSwing(){
		setSize(300, 300);
		setTitle("Hello, Swing");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

//		JButton button = new JButton();
//		add(button);
//		button.setText("My Button");
		
		// 패널은 기본적으로 flowLayout, 프레임은 borderLayout
		// 배치관리자에서 관리
		JPanel panel = new JPanel(); // 컨퍼넌트들을 왼쪽에서 오른쪽으로, 자리가 부족하면 아래로 추가함, 변경 가능
		panel.add(new JButton("panel Button1"));
		panel.add(new JButton("panel Button2"));
		panel.add(new JLabel("panel Label"));
		panel.setBackground(Color.BLUE);
		
		add(panel,  BorderLayout.CENTER); // 컨퍼넌트들이 추가된 패널을 가운데에 추가
		//add(new JButton("My Button 1")); // 이런식으로 추가 가능
		add(new JButton("My Button 2"), BorderLayout.NORTH); // 위쪽에 버튼 추가
		add(new JButton("My Button 3"), BorderLayout.SOUTH); // 레이아웃으로 구획이 나누어 있고 컨퍼넌트를 붙여 표현
		add(new JButton("My Button 4"), BorderLayout.EAST);
		add(new JButton("My Button 5"), BorderLayout.WEST); 
		
		panel.setLayout(null);
		for(int i=0; i<5; i++)
		{
			JButton but = new JButton("Button "+i);
			but.setLocation(100*i, 100*i);
			but.setSize(100,50);
			add(but);
		}
		
		add(panel, BorderLayout.CENTER);
		
		setVisible(true);
	}
	
	public static void main(String[] args) {
		new HelloSwing();

	}

}
