import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import Pusher from 'pusher-js'

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit{

  public indexArr = this.generateIndex()
  public colors = ['pink','red','orange','yellow','yellowgreen','green','lightblue','blue','purple','black']
  public color!: string;
  private cell!:HTMLDivElement;
  private colorBlock!:HTMLDivElement
  private isCell = false;
  private isColor = false;

  constructor(private http: HttpClient) {
  }

  ngOnInit(): void {
//     Pusher.LogToConsole = true;
//
//     const pusher = new Pusher('25291c0752d6089a660d', {
//       cluster: 'eu'
//     });
//
//     const channel = pusher.subscribe('pixel-battle-channel');
//      chanel.bind('pixel-data', data => {
// //         parse data
// //         color = data['color'];
//     });
  }

  public generateIndex(){
    let str=''
    let arr=[]
    for(let i = 1;i<=42;i++){
        for(let j = 1;j<=86;j++){
          str = i+':'+j
          arr.push(str)
        }
      }

      return arr
  }

  public chouseCell(event:Event):void{
    if (!(this.cell == undefined)) {
      this.cell.style.border = '1px solid gray'
    }
    this.cell=<HTMLDivElement>event.target
    this.cell.style.border = '2px solid blue'
    this.isCell=true
  }

  public SaveColor(event:Event):void{
    if(!(this.colorBlock==undefined)){
      this.colorBlock.style.border = '1px solid gray';
    }
    this.colorBlock=<HTMLDivElement>event.target
    this.colorBlock.style.border = '2px solid rgb(80, 80, 197)'
    this.color = this.colorBlock.style.backgroundColor
    this.isColor=true;
  }

  /**
   * paint
   */
  public Paint():void{
    if(this.isCell&&this.isColor){
      this.cell.style.backgroundColor=this.color;
      this.cell.style.border = 'none';
      this.colorBlock.style.border = '1px solid gray';
      this.cell = <HTMLDivElement> document.querySelector('.anreal');
      this.isCell=false;
      this.isColor=false;
      this.http.post('http://127.0.0.1:5000/paint-pixel', {
        test: 'test-message2',
        color: this.color
      }).subscribe();
    }
  }
}
