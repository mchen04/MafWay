import Konva from 'konva';
import { Component } from 'react';

declare module 'react-konva' {
  export interface KonvaNodeProps {
    children?: React.ReactNode;
  }

  export interface StageProps extends KonvaNodeProps {
    width: number;
    height: number;
    onMouseDown?: (e: Konva.KonvaEventObject<MouseEvent>) => void;
    onMouseMove?: (e: Konva.KonvaEventObject<MouseEvent>) => void;
    onMouseUp?: (e: Konva.KonvaEventObject<MouseEvent>) => void;
    className?: string;
  }

  export interface LayerProps extends KonvaNodeProps {
    children?: React.ReactNode;
  }

  export interface LineProps extends KonvaNodeProps {
    points: number[];
    stroke: string;
    strokeWidth: number;
    tension?: number;
    lineCap?: string;
    lineJoin?: string;
  }

  export class Stage extends Component<StageProps> {}
  export class Layer extends Component<LayerProps> {}
  export class Line extends Component<LineProps> {}
}
