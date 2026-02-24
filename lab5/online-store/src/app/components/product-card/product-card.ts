import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-product-card',
  standalone: true, // Добавьте это, если используете Angular 17+
  imports: [],      // И это тоже
  templateUrl: './product-card.html',
  styleUrl: './product-card.css'
})
export class ProductCard {
  // Здесь должна быть логика вашей карточки, например:
  @Input() product: any; 
}