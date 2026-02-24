import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ProductCard } from './product-card';
import { beforeEach, describe, it } from 'node:test';

describe('ProductCard', () => {
  let component: ProductCard;
  let fixture: ComponentFixture<ProductCard>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      // Если компонент Standalone, он должен быть в imports
      imports: [ProductCard] 
    })
    .compileComponents();

    fixture = TestBed.createComponent(ProductCard);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

function expect(component: ProductCard) {
  throw new Error('Function not implemented.');
}
