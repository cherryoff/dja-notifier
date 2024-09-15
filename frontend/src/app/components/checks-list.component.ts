import { Component, Input } from '@angular/core';

@Component({
  standalone: true,
  selector: 'checks-list',
  template: `
    @if (items) {
      <ul>
        @for (check of items; track check.id) {
          <li>{{ check.url }}</li>
        }
      </ul>
    }
    @else {
      <p>No checks available</p>
    }
  `,
  styles: `
    li {
      list-style-type: none;
    }
  `,
})
export class ChecksList {
  @Input() items: any;
}
