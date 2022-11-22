import { Component, OnInit } from '@angular/core';
import { generate } from 'rxjs';

@Component({
  selector: 'app-footter',
  templateUrl: './footter.component.html',
  styleUrls: ['./footter.component.scss']
})
export class FootterComponent implements OnInit{

  public fakeArr = new Array(8450)
  public colors = new Array(10)
  public color!: string;

  constructor() { }

  ngOnInit(): void {
    let someArr = document.getElementsByClassName('colors');
    console.log(someArr)
    // for (let i = 0; i < someArr.length; i++) {
    //   console.log('elem i')
    //   console.log(someArr[i])  
    // }
  }
  public setColor(event:Event):void{
    const elem:HTMLDivElement=<HTMLDivElement>event.target
    elem.style.backgroundColor='red'
  }
  public SaveColor(event:Event):void{
    const elem:HTMLDivElement=<HTMLDivElement>event.target
    this.color = elem.style.backgroundColor
    console.log(this.color)
  }

}