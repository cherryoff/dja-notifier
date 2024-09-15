import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ChecksList } from './components/checks-list.component';
import { DataService } from './data.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, ChecksList],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  checksData: any;

  constructor(private dataService: DataService) {}

  ngOnInit() {
    this.dataService.getData().subscribe((data) => {
      this.checksData = data;
    });
  }
}
